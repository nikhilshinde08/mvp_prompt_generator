"""Performance metrics system for the GitHub MVP Generator."""

import json
import os
import time
from typing import Dict, Any, List
from datetime import datetime


class PerformanceMetrics:
    """Tracks and manages performance metrics for the system."""
    
    def __init__(self, metrics_file: str = "performance_metrics.json"):
        self.metrics_file = metrics_file
        self.metrics_data = self._load_metrics()
        self.current_session = {
            "start_time": time.time(),
            "operations": []
        }
    
    def _load_metrics(self) -> Dict[str, Any]:
        """Load existing metrics from file."""
        if os.path.exists(self.metrics_file):
            try:
                with open(self.metrics_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return self._get_default_metrics()
        return self._get_default_metrics()
    
    def _get_default_metrics(self) -> Dict[str, Any]:
        """Get default metrics structure."""
        return {
            "total_operations": 0,
            "successful_operations": 0,
            "failed_operations": 0,
            "average_response_time": 0.0,
            "provider_performance": {},
            "operation_types": {},
            "last_updated": datetime.now().isoformat()
        }
    
    def _save_metrics(self):
        """Save metrics to file."""
        self.metrics_data["last_updated"] = datetime.now().isoformat()
        try:
            with open(self.metrics_file, 'w') as f:
                json.dump(self.metrics_data, f, indent=2)
        except IOError as e:
            print(f"Warning: Could not save performance metrics: {e}")
    
    def start_operation(self, operation_type: str, provider: str = None) -> Dict[str, Any]:
        """Start tracking an operation."""
        operation = {
            "operation_type": operation_type,
            "provider": provider,
            "start_time": time.time(),
            "status": "in_progress"
        }
        self.current_session["operations"].append(operation)
        return operation
    
    def end_operation(self, operation: Dict[str, Any], success: bool = True, error: str = None):
        """End tracking an operation."""
        operation["end_time"] = time.time()
        operation["duration"] = operation["end_time"] - operation["start_time"]
        operation["status"] = "success" if success else "failed"
        if error:
            operation["error"] = error
        
        # Update metrics data
        self.metrics_data["total_operations"] += 1
        if success:
            self.metrics_data["successful_operations"] += 1
        else:
            self.metrics_data["failed_operations"] += 1
        
        # Update operation type stats
        op_type = operation["operation_type"]
        if op_type not in self.metrics_data["operation_types"]:
            self.metrics_data["operation_types"][op_type] = {
                "count": 0,
                "total_time": 0.0,
                "success_count": 0,
                "failed_count": 0
            }
        
        self.metrics_data["operation_types"][op_type]["count"] += 1
        self.metrics_data["operation_types"][op_type]["total_time"] += operation["duration"]
        if success:
            self.metrics_data["operation_types"][op_type]["success_count"] += 1
        else:
            self.metrics_data["operation_types"][op_type]["failed_count"] += 1
        
        # Update provider stats if provider is specified
        if operation["provider"]:
            provider = operation["provider"]
            if provider not in self.metrics_data["provider_performance"]:
                self.metrics_data["provider_performance"][provider] = {
                    "count": 0,
                    "total_time": 0.0,
                    "success_count": 0,
                    "failed_count": 0
                }
            
            self.metrics_data["provider_performance"][provider]["count"] += 1
            self.metrics_data["provider_performance"][provider]["total_time"] += operation["duration"]
            if success:
                self.metrics_data["provider_performance"][provider]["success_count"] += 1
            else:
                self.metrics_data["provider_performance"][provider]["failed_count"] += 1
        
        # Update average response time
        total_time = sum(
            op.get("duration", 0) for ops in self.metrics_data["operation_types"].values()
            for op in [ops] if isinstance(op, dict)
        )
        total_count = sum(
            op.get("count", 0) for ops in self.metrics_data["operation_types"].values()
            for op in [ops] if isinstance(op, dict)
        )
        self.metrics_data["average_response_time"] = total_time / total_count if total_count > 0 else 0.0
        
        self._save_metrics()
    
    def get_performance_summary(self) -> Dict[str, Any]:
        """Get a summary of performance metrics."""
        # Calculate success rates
        total_ops = self.metrics_data["total_operations"]
        success_rate = (
            self.metrics_data["successful_operations"] / total_ops * 100
            if total_ops > 0 else 0
        )
        
        # Calculate average times for operation types
        operation_averages = {}
        for op_type, stats in self.metrics_data["operation_types"].items():
            count = stats["count"]
            total_time = stats["total_time"]
            avg_time = total_time / count if count > 0 else 0
            success_rate_op = (stats["success_count"] / count * 100) if count > 0 else 0
            operation_averages[op_type] = {
                "average_time": avg_time,
                "success_rate": success_rate_op,
                "total_count": count
            }
        
        # Calculate provider performance
        provider_performance = {}
        for provider, stats in self.metrics_data["provider_performance"].items():
            count = stats["count"]
            total_time = stats["total_time"]
            avg_time = total_time / count if count > 0 else 0
            success_rate_prov = (stats["success_count"] / count * 100) if count > 0 else 0
            provider_performance[provider] = {
                "average_time": avg_time,
                "success_rate": success_rate_prov,
                "total_count": count
            }
        
        return {
            "total_operations": total_ops,
            "success_rate": success_rate,
            "failed_operations": self.metrics_data["failed_operations"],
            "average_response_time": self.metrics_data["average_response_time"],
            "operation_performance": operation_averages,
            "provider_performance": provider_performance,
            "last_updated": self.metrics_data["last_updated"]
        }
    
    def get_session_summary(self) -> Dict[str, Any]:
        """Get a summary of the current session."""
        completed_ops = [op for op in self.current_session["operations"] if op["status"] != "in_progress"]
        if not completed_ops:
            return {"message": "No operations completed in this session"}
        
        total_time = sum(op["duration"] for op in completed_ops)
        avg_time = total_time / len(completed_ops)
        
        success_count = sum(1 for op in completed_ops if op["status"] == "success")
        success_rate = success_count / len(completed_ops) * 100
        
        return {
            "session_duration": time.time() - self.current_session["start_time"],
            "operations_completed": len(completed_ops),
            "average_response_time": avg_time,
            "success_rate": success_rate
        }


# Global performance metrics instance
performance_metrics = PerformanceMetrics()
from dataclasses import dataclass


@dataclass
class LearningStatistics:
    num_training_instances: int = 0
    num_selected_training_instances: int = 0
    num_states_in_selected_training_instances: int = 0
    num_features_in_pool: int = 0
    num_cpu_seconds: float = 0
    num_peak_memory_mb: float = 0

    def print(self):
        print("LearningStatistics:")
        print("    num_training_instances:", self.num_training_instances)
        print("    num_selected_training_instances:", self.num_selected_training_instances)
        print("    num_states_in_selected_training_instances:", self.num_states_in_selected_training_instances)
        print("    num_features_in_pool:", self.num_features_in_pool)
        print("    num_cpu_seconds: {:.2f} seconds".format(self.num_cpu_seconds))
        print("    num_peak_memory_mb: {:.2f} MB".format(self.num_peak_memory_mb))

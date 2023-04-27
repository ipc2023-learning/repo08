


def training_instances(benchmark_dir, instance_names):
    instance_filenames = []
    for instance_name in instance_names:
        instance_filenames.append(BENCHMARK_DIR / "gripper" / "instances" / instance_name)
    return instance_filenames


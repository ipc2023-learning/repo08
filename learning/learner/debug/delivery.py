from sketch_learning.util.misc import update_dict


def experiments():
    base = dict(
        domain_dir="delivery",
    )

    exps = dict()

    strips_base = update_dict(
        base,
        domain="domain",
    )

    exps["sketch_debug"] = update_dict(
        strips_base,
        pipeline="sketch_pipeline",
        instances=training_instances(),
        debug_features=["n_count(c_not(c_equal(r_primitive(at_g,0,1),r_primitive(at,0,1))))",  # 5
                        "b_empty(c_primitive(empty,0))",  # 2
                        "n_concept_distance(c_some(r_inverse(r_primitive(at,0,1)),c_primitive(truck,0)), r_primitive(adjacent,0,1), c_primitive(at_g,1))",  # 7
                        "n_concept_distance(c_some(r_inverse(r_primitive(at,0,1)),c_primitive(truck,0)), r_primitive(adjacent,0,1), c_and(c_all(r_inverse(r_primitive(at_g,0,1)),c_bot),c_some(r_inverse(r_primitive(at,0,1)),c_primitive(package,0))))",  # 15
                        # "n_concept_distance(c_some(r_inverse(r_primitive(at,0,1)),c_primitive(truck,0)),r_primitive(adjacent,0,1),c_not(c_all(r_inverse(r_primitive(at,0,1)),c_equal(r_primitive(at,0,1),r_primitive(at_g,0,1)))))" alternative feature
        ],
    )

    exps["sketch"] = update_dict(
        strips_base,
        pipeline="sketch_pipeline",
        instances=training_instances(),
        max_states_per_instance=2000,
    )

    exps["hierarchy"] = update_dict(
        strips_base,
        pipeline="hierarchy_pipeline",
        instances=training_instances(),
        # instances=["instance_3_2_3"],
        max_states_per_instance=2000,
    )

    exps["hierarchy_debug"] = update_dict(
        strips_base,
        pipeline="hierarchy_pipeline",
        instances=training_instances(),
        debug_features=["n_count(r_and(r_primitive(at,0,1),r_primitive(at_g,0,1)))",
                        "b_empty(c_primitive(empty,0))",
                        "n_count(r_and(r_primitive(at,0,1),r_primitive(at_g,0,1)))",
                        "n_concept_distance(c_some(r_inverse(r_primitive(at,0,1)),c_primitive(truck,0)),r_primitive(adjacent,0,1),c_some(r_inverse(r_primitive(at,0,1)),c_primitive(package,0)))",
                        "n_concept_distance(c_some(r_inverse(r_primitive(at,0,1)),c_primitive(truck,0)),r_primitive(adjacent,0,1),c_some(r_inverse(r_primitive(at_g,0,1)),c_top))",
                        "n_concept_distance(c_some(r_inverse(r_primitive(at,0,1)),c_primitive(truck,0)), r_primitive(adjacent,0,1), c_and(c_all(r_inverse(r_primitive(at_g,0,1)),c_bot),c_some(r_inverse(r_primitive(at,0,1)),c_primitive(package,0))))"],
        max_states_per_instance=2000,
    )
    return exps


def training_instances():
    return [f"instance_{h}_{w}_{n}_{seed}" for h in range(1,4) for w in range(1,4) for n in range(1,3) for seed in range(0,10) ]

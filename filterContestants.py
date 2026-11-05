import polars as pl
def contestant_age_summary(gender, contestants):
    #filters the contestants
    gender_contestants = contestants.filter(pl.col("gender") == gender)

    #calc the statistics for engaged 
    engaged_contestants = gender_contestants.filter(pl.col("engaged") == 1)
    avg_age_engaged_contestants = engaged_contestants.select(pl.mean("age").cast(pl.Int64))
    youngest_engaged_contestants = engaged_contestants.select(pl.min("age"))
    oldest_engaged_contestants = engaged_contestants.select(pl.max("age"))
    median_engaged_contestants = engaged_contestants.select(pl.median("age"))
    print(f"--------------Engaged {gender} Contestant Summary--------------------")
    print("mean")
    print(avg_age_engaged_contestants)
    print("youngest contestant")
    print(youngest_engaged_contestants)
    print("oldest contestant")
    print(oldest_engaged_contestants)
    print("median")
    print(median_engaged_contestants)
    #calc the statistics for single
    single_contestants = gender_contestants.filter(pl.col("engaged") == 0)
    avg_age_single_contestants = single_contestants.select(pl.mean('age').cast(pl.Int64))
    youngest_single_contestants = single_contestants.select(pl.min("age"))
    oldest_single_contestants = single_contestants.select(pl.max("age"))
    median_single_contestants = single_contestants.select(pl.median("age"))
    print(f"--------------Single {gender} Contestant Summary--------------------")
    print("mean")
    print(avg_age_single_contestants)
    print("youngest contestant")
    print(youngest_single_contestants)
    print("oldest contestant")
    print(oldest_single_contestants)
    print("median")
    print(median_single_contestants)

    return [gender_contestants,engaged_contestants, single_contestants]

def age_group_enagement(contestants):
    results_by_gender = (
    contestants.group_by(["age_group"])
    .agg(
        pl.len().alias("total_contestants"),
        pl.col("engaged").sum().alias("engaged_contestants "), 
        (pl.col("engaged").mean() * 100).alias("engagement_rate")
    )
    .sort(["age_group"])
    )
    return results_by_gender
hadoop dfs -rmr /user/sadhikar/weblog/simple_stats
hadoop jar /usr/lib/hadoop/contrib/streaming/hadoop-streaming-1.0.3-Intel.jar \
	-file ./simple_stats_mapper.py \
	-file ./simple_stats_reducer.py \
	-mapper ./simple_stats_mapper.py \
	-reducer ./simple_stats_reducer.py \
	-input /user/sadhikar/weblog/input \
	-output /user/sadhikar/weblog/simple_stats


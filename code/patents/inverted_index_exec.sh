hadoop dfs -rmr /user/sadhikar/citations/inverted_index
hadoop jar /usr/lib/hadoop/contrib/streaming/hadoop-streaming-1.0.3-Intel.jar \
	-file ./inverted_index_mapper.py \
	-file ./inverted_index_reducer.py \
	-mapper ./inverted_index_mapper.py \
	-reducer ./inverted_index_reducer.py \
	-input /user/sadhikar/citations/input \
	-output /user/sadhikar/citations/inverted_index


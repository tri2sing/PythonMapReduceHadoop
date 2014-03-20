hadoop dfs -rmr /user/sadhikar/patents_citations/small
hadoop jar /usr/lib/hadoop/contrib/streaming/hadoop-streaming-1.0.3-Intel.jar \
	-file ./relational_join_mapper.py \
	-file ./relational_join_reducer.py \
	-mapper ./relational_join_mapper.py \
	-reducer ./relational_join_reducer.py \
	-input /user/sadhikar/patents_citations/test \
	-output /user/sadhikar/patents_citations/small


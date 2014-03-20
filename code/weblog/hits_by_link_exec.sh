hadoop dfs -rmr /user/sadhikar/weblog/hits_by_link
hadoop jar /usr/lib/hadoop/contrib/streaming/hadoop-streaming-1.0.3-Intel.jar \
	-file ./hits_by_link_mapper.py \
	-file ./hits_by_link_reducer.py \
	-mapper ./hits_by_link_mapper.py \
	-reducer ./hits_by_link_reducer.py \
	-input /user/sadhikar/weblog/input \
	-output /user/sadhikar/weblog/hits_by_link


hadoop dfs -rmr /user/sadhikar/weblog/sorted_links
hadoop jar /usr/lib/hadoop/contrib/streaming/hadoop-streaming-1.0.3-Intel.jar \
	-file ./sorted_links_mapper.py \
	-file ./sorted_links_reducer.py \
	-mapper ./sorted_links_mapper.py \
	-reducer ./sorted_links_reducer.py \
	-input /user/sadhikar/weblog/input \
	-output /user/sadhikar/weblog/sorted_links


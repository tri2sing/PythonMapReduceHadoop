hadoop dfs -rmr /user/sadhikar/envvars/output
hadoop jar /usr/lib/hadoop/contrib/streaming/hadoop-streaming-1.0.3-Intel.jar \
	-file ./env_mapper.py \
	-file ./env_reducer.py \
	-mapper ./env_mapper.py \
	-reducer ./env_reducer.py \
	-input /user/sadhikar/envvars/input\
	-output /user/sadhikar/envvars/output


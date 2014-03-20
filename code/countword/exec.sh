hadoop dfs -rmr /user/sadhikar/gutenberg/output
hadoop jar /usr/lib/hadoop/contrib/streaming/hadoop-streaming-1.0.3-Intel.jar \
	-file ./mapper.py \
	-file ./reducer.py \
	-mapper ./mapper.py \
	-combiner ./reducer.py \
	-reducer ./reducer.py \
	-input /user/sadhikar/gutenberg/input \
	-output /user/sadhikar/gutenberg/output 


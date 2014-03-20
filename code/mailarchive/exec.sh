# Phase 1.  Count the occurrences of each subject
hadoop dfs -rmr /user/sadhikar/mailarchive/intermediate
hadoop jar /usr/lib/hadoop/contrib/streaming/hadoop-streaming-1.0.3-Intel.jar \
	-file ./count_mapper.py \
	-file ./count_reducer.py \
	-file ./parsembox.py \
	-mapper ./count_mapper.py \
	-reducer ./count_reducer.py \
	-input /user/sadhikar/mailarchive/input \
	-output /user/sadhikar/mailarchive/intermediate 

# Phase 2: Sort by the number of occurrences.
hadoop dfs -rmr /user/sadhikar/mailarchive/final
hadoop jar /usr/lib/hadoop/contrib/streaming/hadoop-streaming-1.0.3-Intel.jar \
	-D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
	-D  mapred.text.key.comparator.options=-nr \
	-file ./sort_mapper.py \
	-file ./sort_reducer.py \
	-mapper ./sort_mapper.py \
	-reducer ./sort_reducer.py \
	-input /user/sadhikar/mailarchive/intermediate \
	-output /user/sadhikar/mailarchive/final 


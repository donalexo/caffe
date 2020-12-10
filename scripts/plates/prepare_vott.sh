# Rename files. Caffe uses trainval.txt and test.txt
mv $CAFFE_HOME/data/plates/ImageSets/Main/plate_train.txt $CAFFE_HOME/data/plates/ImageSets/Main/trainval.txt
mv $CAFFE_HOME/data/plates/ImageSets/Main/plate_val.txt $CAFFE_HOME/data/plates/ImageSets/Main/test.txt

# Remove everything after the file extension in trainval.txt and test.txt
sed -i -E "s/\.jpg.+//" $CAFFE_HOME/data/plates/ImageSets/Main/trainval.txt
sed -i -E "s/\.jpg.+//" $CAFFE_HOME/data/plates/ImageSets/Main/test.txt

# Copy correct labelmaps to data dir and remove files exported by vott
cp $CAFFE_HOME/scripts/plates/files/labelmap_plates.prototxt $CAFFE_HOME/data/plates/
rm $CAFFE_HOME/data/plates/pascal_label_map.pbtxt

import os
import xml.etree.ElementTree


def cast_bndbox_to_int(annotations_dir):
    for file_name in os.listdir(annotations_dir):
        file_id = file_name[:-4]
        file_path = os.path.join(annotations_dir, file_name)
        print 'converting', file_path
        # Open original file
        et = xml.etree.ElementTree.parse(file_path)
        root = et.getroot()
        for child in root.findall('object'):
            for box in child.findall('bndbox'):
                
                xmin_elem = box.find('xmin')
                ymin_elem = box.find('ymin')
                xmax_elem = box.find('xmax')
                ymax_elem = box.find('ymax')

                xmin_elem.text = str(int(round(float(xmin_elem.text))))
                ymin_elem.text = str(int(round(float(ymin_elem.text))))
                xmax_elem.text = str(int(round(float(xmax_elem.text))))
                ymax_elem.text = str(int(round(float(ymax_elem.text))))
                
        et.write(file_path)


if __name__ == '__main__':
    cast_bndbox_to_int('../../data/plates/Annotations')

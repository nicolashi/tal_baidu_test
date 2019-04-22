
GALLERY_FILE="gallery_img"
GALLERY_DIR="../0_TEST_align2_gallery"
while read img label;do
  echo "$img to $GALLERY_DIR/$label.jpg"
  mv $img "$GALLERY_DIR/$label.jpg"
  mv "${img%/*}" $label
done < $GALLERY_FILE

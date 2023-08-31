import napari


def main(image_path, model_path, output_path, display_results=True, use_gpu=False):
    """
    Load image, segment it and save the resulting mask

    Parameters
    ----------
    image_path: str
        input image path
    model_path: str
        pretrained model path
    output_path: str
        output directory
    display_results: bool, default True
        if True display input image and segmentation mask in napari
    use_gpu: bool, default False
        if True use GPU for the segmentation
    """

    # Read the image

    if display_results: # Open image in napari
        # Only import PyQt5 if needed (no need for PyQt5 dependency if display_results is False)
        from PyQt5.QtGui import QCursor
        from PyQt5.QtCore import Qt
        from PyQt5.QtWidgets import QMessageBox

        viewer_images = napari.Viewer(title=image_path)
        #viewer_images.add_image(image_opened, name="Input image")
        
        
        # Set cursor to BusyCursor
        napari.qt.get_app().setOverrideCursor(QCursor(Qt.BusyCursor))
        napari.qt.get_app().processEvents()

        # Show activity dock & add napari progress bar
        viewer_images.window._status_bar._toggle_activity_dock(True)
    
    # Perform segmentation
    # Save the segmented mask

    if display_results:  # Open the segmented mask in napari
            # Stop logging into napari window & restore cursor
            napari.qt.get_app().restoreOverrideCursor()
            viewer_images.window._status_bar._toggle_activity_dock(False)
            
            # Show mask in napari
            #layer_mask = viewer_images.add_labels(mask, name="Mask")
            #layer_mask.editable = False # Do not allow edition


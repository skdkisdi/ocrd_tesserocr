import os
import shutil

from test.base import TestCase, main, assets

from ocrd.resolver import Resolver
from ocrd_tesserocr.segment_region import TesserocrSegmentRegion
from ocrd_tesserocr.segment_line import TesserocrSegmentLine

METS_HEROLD_SMALL = assets.url_of('SBB0000F29300010000/mets_one_file.xml')

WORKSPACE_DIR = '/tmp/pyocrd-test-segment-line-tesserocr'

class TestProcessorSegmentLineTesseract(TestCase):

    def setUp(self):
        if os.path.exists(WORKSPACE_DIR):
            shutil.rmtree(WORKSPACE_DIR)
        os.makedirs(WORKSPACE_DIR)

    def runTest(self):
        resolver = Resolver()
        workspace = resolver.workspace_from_url(METS_HEROLD_SMALL, directory=WORKSPACE_DIR)
        TesserocrSegmentRegion(workspace, input_file_grp="INPUT", output_file_grp="OCR-D-SEG-BLOCK").process()
        #  workspace.save_mets()
        TesserocrSegmentLine(workspace, input_file_grp="OCR-D-SEG-BLOCK", output_file_grp="OCR-D-SEG-LINE").process()
        workspace.save_mets()

if __name__ == '__main__':
    main()

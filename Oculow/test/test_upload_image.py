from unittest import TestCase

from Oculow import oculow


class TestUpload_image(TestCase):
    def test_upload_image(self):
        oculow.set_api_key("iCyZc90jJIVJJEcJUYx/9uP8Eyk3b3SD", "+Le1k0t/htqb1rhE1nkri6C7JOW85yWQ")
        oculow.set_app_id("oculow")
        oculow.set_baseline_management(oculow.ASSISTED)
        oculow.set_comparison_logic(oculow.PIXEL_DIFF)
        oculow.viewport_height=99999
        oculow.viewport_width=99999
        out = oculow.upload_image("C:\\Users\\potos\\Desktop\\error_example.PNG")
        print(out)

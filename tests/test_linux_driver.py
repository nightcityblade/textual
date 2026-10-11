import sys
from unittest.mock import Mock

import pytest


@pytest.mark.skipif(sys.platform == "win32", reason="LinuxDriver is unavailable")
def test_disable_mouse_support_disables_pixel_mode() -> None:
    """Pixel mouse reporting should be disabled when it was enabled."""
    from textual.drivers.linux_driver import LinuxDriver

    driver = Mock(spec=LinuxDriver)
    driver._mouse = True
    driver._mouse_pixels = True

    LinuxDriver._disable_mouse_support(driver)

    driver.write.assert_any_call("\x1b[?1016l")

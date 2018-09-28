def test_systemd_overlay_file(host):
    f = host.file("/etc/systemd/system/cockpit.socket.d/listen.conf")
    assert f.exists
    assert f.is_file

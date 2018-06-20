"""
This class holds the code to make camera objects.
"""


class Camera(object):
    """
    Represent a single camera
    """
    def __init__(self, cameraID, camera_type, source, lat, lng, country, state, city,
                 resolution_width, resolution_height, is_active_image,
                 is_active_video, utc_offset, timezone_id,
                 timezone_name, reference_logo, reference_url):
        self.cameraID = cameraID
        self.camera_type = camera_type
        self.source = source
        self.lat = lat
        self.lng = lng
        self.country = country
        self.state = state
        self.city = city
        self.resolution_width = resolution_width
        self.resolution_height = resolution_height
        self.is_active_image = is_active_image
        self.is_active_video = is_active_video
        self.utc_offset = utc_offset
        self.timezone_id = timezone_id
        self.timezone_name = timezone_name
        self.reference_logo = reference_logo
        self.reference_url = reference_url
class IPCamera(Camera):
    """
    Represent a single ip_camera
    This is a subclass of Camera
    """
#<<<<<<< Updated upstream
    def __init__(self, cameraID, camera_type, source, lat, lng, country, state,
                 city, resolution_width, resolution_height, is_active_image,
                 is_active_video, utc_offset, timezone_id, timezone_name,
                 reference_logo, reference_url, ip, port, brand, model, image_path, video_path):
        self.ip = ip
        self.port = port
        self.brand = brand
        self.model = model
        self.image_path = image_path
        self.video_path = video_path
        super(IPCamera, self).__init__(cameraID, camera_type, source, lat, lng,
                                       country, state, city, resolution_width,
                                       resolution_height, is_active_image, is_active_video,
                                       utc_offset, timezone_id, timezone_name,
                                       reference_logo, reference_url)

#=======
    # TODO: define extra retrieval attributes and constructor of ip camera object
    # replace others with desired field names
    def __init__(self,cameraID, camera_type, source, lat, lng, country, state, city, resolution_width
                , resolution_height, is_active_image, is_active_video, utc_offset, timezone_id
                , timezone_name, reference_logo, reference_url, ip,port,brand,model,image_path,video_path):
                self.ip = ip
                self.port = port
                self.brand = brand
                self.model = model
                self.image_path = image_path
                self.video_path = video_path
                super(IPCamera, self).__init__(cameraID, camera_type, source, lat, lng, country, state, city, resolution_width
                , resolution_height, is_active_image, is_active_video, utc_offset, timezone_id
                , timezone_name, reference_logo, reference_url)
    def asdict(self):
        data = super().asdict()
        data['retrieval'] = {
            "ip": self.ip,
            "port": self.port,
            "brand": self.brand,
            "model": self.model,
            "image_path": self.image_path,
            "video_path": self.video_path
        }
#>>>>>>> Stashed changes

class NonIPCamera(Camera):
    """
    Represent a non-IP camera.
    This is a subclass of Camera
    """
    def __init__(self, cameraID, camera_type, source, lat, lng, country, state, city,
                 resolution_width, resolution_height, is_active_image, is_active_video,
                 utc_offset, timezone_id, timezone_name, reference_logo,
                 reference_url, snapshot_url):
        self.snapshot_url = snapshot_url
        super(NonIPCamera, self).__init__(cameraID, camera_type, source, lat, lng,
                                          country, state, city, resolution_width,
                                          resolution_height, is_active_image,
                                          is_active_video, utc_offset,
                                          timezone_id, timezone_name,
                                          reference_logo, reference_url)


class StreamCamera(Camera):
    """
    Represent a Stream camera.
    This is a subclass of Camera
    """
    def __init__(self, cameraID, camera_type, source, lat, lng, country, state, city,
                 resolution_width, resolution_height, is_active_image, is_active_video,
                 utc_offset, timezone_id, timezone_name, reference_logo, reference_url,
                 m3u8_url):
        self.m3u8_url = m3u8_url
        super(StreamCamera, self).__init__(cameraID, camera_type, source, lat, lng,
                                           country, state, city, resolution_width,
                                           resolution_height, is_active_image,
                                           is_active_video, utc_offset,
                                           timezone_id, timezone_name,
                                           reference_logo, reference_url)

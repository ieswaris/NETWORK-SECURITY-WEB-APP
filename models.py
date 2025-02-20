from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)


class UserPredictModel(models.Model):
    flow_duration = models.FloatField()
    fwd_pkts_tot = models.FloatField()
    bwd_pkts_tot = models.FloatField()
    fwd_data_pkts_tot = models.FloatField()
    bwd_data_pkts_tot = models.FloatField()
    fwd_pkts_per_sec = models.FloatField()
    bwd_pkts_per_sec = models.FloatField()
    flow_pkts_per_sec = models.FloatField()
    down_up_ratio = models.FloatField()
    fwd_header_size_tot = models.FloatField()
    fwd_header_size_min = models.FloatField()
    fwd_header_size_max = models.FloatField()
    bwd_header_size_tot = models.FloatField()
    bwd_header_size_min = models.FloatField()
    bwd_header_size_max = models.FloatField()
    flow_FIN_flag_count = models.IntegerField()
    flow_SYN_flag_count = models.IntegerField()
    flow_RST_flag_count = models.IntegerField()
    fwd_PSH_flag_count = models.IntegerField()
    bwd_PSH_flag_count = models.IntegerField()
    flow_ACK_flag_count = models.IntegerField()
    fwd_URG_flag_count = models.IntegerField()
    bwd_URG_flag_count = models.IntegerField()
    flow_CWR_flag_count = models.IntegerField()
    flow_ECE_flag_count = models.IntegerField()
    fwd_pkts_payload_min = models.FloatField()
    fwd_pkts_payload_max = models.FloatField()
    fwd_pkts_payload_tot = models.FloatField()
    fwd_pkts_payload_avg = models.FloatField()
    fwd_pkts_payload_std = models.FloatField()
    bwd_pkts_payload_min = models.FloatField()
    bwd_pkts_payload_max = models.FloatField()
    bwd_pkts_payload_tot = models.FloatField()
    bwd_pkts_payload_avg = models.FloatField()
    bwd_pkts_payload_std = models.FloatField()
    flow_pkts_payload_min = models.FloatField()
    flow_pkts_payload_max = models.FloatField()
    flow_pkts_payload_tot = models.FloatField()
    flow_pkts_payload_avg = models.FloatField()
    flow_pkts_payload_std = models.FloatField()
    fwd_bulk_packets = models.IntegerField()
    bwd_bulk_packets = models.IntegerField()
    fwd_bulk_rate = models.FloatField()
    bwd_bulk_rate = models.FloatField()
    fwd_init_window_size = models.IntegerField()
    bwd_init_window_size = models.IntegerField()
    fwd_last_window_size = models.IntegerField()
    label=models.CharField(max_length=300)

    def __str__(self):
        return f" Prediction  - {self.label}"


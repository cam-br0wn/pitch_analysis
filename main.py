import csv


class Player:
    def __init__(self):
        self.player_name = ""
        self.filepath = ""

        # Average pitch velocities
        self.avg_fb_vel = 0
        self.avg_cb_vel = 0
        self.avg_sl_vel = 0
        self.avg_ch_vel = 0

        # Average pitch spin rates
        self.avg_fb_spin = 0
        self.avg_cb_spin = 0
        self.avg_sl_spin = 0
        self.avg_ch_spin = 0

        # Average pitch extension values
        self.avg_ext = 0  # Average extension across all pitches
        self.avg_ext_fb = 0
        self.avg_ext_cb = 0
        self.avg_ext_sl = 0
        self.avg_ext_ch = 0

        self.rel_sp_arr = []
        self.rel_h_arr = []
        self.rel_s_arr = []
        self.ext_arr = []
        self.pitch_type_arr = []
        self.spin_rate_arr = []

    def generate_arrays(self):
        line_count = 0
        release_speed = []
        release_height = []
        release_side = []
        extension = []
        pitch_type = []
        spin_rate = []
        self.filepath = input("Enter filepath: ")
        default_filepath = 'C:/Users/cakbro/Documents/Schwartz_Pitching.csv'
        if len(self.filepath) == 0:
            self.filepath = default_filepath
        with open(self.filepath) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')  # ASSUMES COMMA SEPARATION AND CARRIAGE RETURNS
            for row in csv_reader:
                if len(row) > 0 and line_count > 0:
                    for i in range(16):
                        if row[i] == '':
                            row[i] = '--'
                    release_speed.append(row[0])
                    release_height.append(row[3])
                    release_side.append(row[4])
                    extension.append(row[5])
                    pitch_type.append(row[14])
                    spin_rate.append(row[15])
                    if self.player_name == "":
                        self.player_name = row[1]
                line_count += 1

        self.rel_sp_arr = release_speed
        self.rel_h_arr = release_height
        self.rel_s_arr = release_side
        self.ext_arr = extension
        self.pitch_type_arr = pitch_type
        self.spin_rate_arr = spin_rate

    def get_avg_fbv(self):
        fb_vel_sum = 0.0
        fb_qt = 0
        for i in range(len(self.rel_sp_arr)):
            if self.rel_sp_arr[i] != "--" and self.pitch_type_arr[i] == "Fastball":
                fb_vel_sum += float(self.rel_sp_arr[i])
                fb_qt += 1
        self.avg_fb_vel = fb_vel_sum / fb_qt
        if fb_qt > 0:
            self.avg_fb_vel = round(fb_vel_sum / fb_qt, 2)
        else:
            self.avg_fb_vel = "* No fastball velos measured this session *"

    def get_avg_cbv(self):
        cb_vel_sum = 0.0
        cb_qt = 0
        for i in range(len(self.rel_sp_arr)):
            if self.rel_sp_arr[i] != "--" and self.pitch_type_arr[i] == "Curveball":
                cb_vel_sum += float(self.rel_sp_arr[i])
                cb_qt += 1
        self.avg_cb_vel = cb_vel_sum / cb_qt
        if cb_qt > 0:
            self.avg_cb_vel = round(cb_vel_sum / cb_qt, 2)
        else:
            self.avg_cb_vel = "* No curveball velos measured this session *"

    def get_avg_slv(self):
        sl_vel_sum = 0.0
        sl_qt = 0
        for i in range(len(self.rel_sp_arr)):
            if self.rel_sp_arr[i] != "--" and self.pitch_type_arr[i] == "Slider":
                sl_vel_sum += float(self.rel_sp_arr[i])
                sl_qt += 1
        if sl_qt > 0:
            self.avg_sl_vel = round(sl_vel_sum / sl_qt, 2)
        else:
            self.avg_sl_vel = "* No slider velos measured this session *"

    def get_avg_chv(self):
        ch_vel_sum = 0.0
        ch_qt = 0
        for i in range(len(self.rel_sp_arr)):
            if self.rel_sp_arr[i] != "--" and self.pitch_type_arr[i] == "Changeup":
                ch_vel_sum += float(self.rel_sp_arr[i])
                ch_qt += 1
        if ch_qt > 0:
            self.avg_ch_vel = round(ch_vel_sum / ch_qt, 2)
        else:
            self.avg_ch_vel = "* No changeup velos measured this session *"

    def get_avg_fbs(self):
        fb_spin_sum = 0
        fb_qt = 0
        for i in range(len(self.spin_rate_arr)):
            if self.spin_rate_arr[i] != '--' and self.pitch_type_arr[i] == "Fastball":
                fb_spin_sum += int(self.spin_rate_arr[i])
                fb_qt += 1
        if fb_qt > 0:
            self.avg_fb_spin = round(fb_spin_sum / fb_qt, 2)
        else:
            self.avg_fb_spin = "* No fastball spin rates measured this session *"

    def get_avg_cbs(self):
        cb_spin_sum = 0
        cb_qt = 0
        for i in range(len(self.spin_rate_arr)):
            if self.spin_rate_arr[i] != '--' and self.pitch_type_arr[i] == "Curveball":
                cb_spin_sum += int(self.spin_rate_arr[i])
                cb_qt += 1
        if cb_qt > 0:
            self.avg_cb_spin = round(cb_spin_sum / cb_qt, 2)
        else:
            self.avg_cb_spin = "* No curveball spin rates measured this session *"

    def get_avg_sls(self):
        sl_spin_sum = 0
        sl_qt = 0
        for i in range(len(self.spin_rate_arr)):
            if self.spin_rate_arr[i] != '--' and self.pitch_type_arr[i] == "Slider":
                sl_spin_sum += int(self.spin_rate_arr[i])
                sl_qt += 1
        if sl_qt > 0:
            self.avg_sl_spin = round(sl_spin_sum / sl_qt, 2)
        else:
            self.avg_sl_spin = "* No slider spin rates measured this session *"

    def get_avg_chs(self):
        ch_spin_sum = 0
        ch_qt = 0
        for i in range(len(self.spin_rate_arr)):
            if self.spin_rate_arr[i] != '--' and self.pitch_type_arr[i] == "Changeup":
                ch_spin_sum += int(self.spin_rate_arr[i])
                ch_qt += 1
        if ch_qt > 0:
            self.avg_ch_spin = round(ch_spin_sum / ch_qt, 2)
        else:
            self.avg_ch_spin = "* No changeup spin rates measured this session *"

    def get_avg_fbe(self):
        fb_ext_sum = 0.0
        fb_qt = 0
        for i in range(len(self.ext_arr)):
            if self.ext_arr[i] != '--' and self.pitch_type_arr[i] == 'Fastball':
                fb_ext_sum += float(self.ext_arr[i])
                fb_qt += 1
        if fb_qt > 0:
            self.avg_ext_fb = round(fb_ext_sum / fb_qt, 2)
        else:
            self.avg_ext_fb = "* No fastball extension measurements taken this session *"

    def get_avg_cbe(self):
        cb_ext_sum = 0.0
        cb_qt = 0
        for i in range(len(self.ext_arr)):
            if self.ext_arr[i] != '--' and self.pitch_type_arr[i] == 'Curveball':
                cb_ext_sum += float(self.ext_arr[i])
                cb_qt += 1
        if cb_qt > 0:
            self.avg_ext_cb = round(cb_ext_sum / cb_qt, 2)
        else:
            self.avg_ext_cb = "* No curveball extension measurements taken this session *"

    def get_avg_sle(self):
        sl_ext_sum = 0.0
        sl_qt = 0
        for i in range(len(self.ext_arr)):
            if self.ext_arr[i] != '--' and self.pitch_type_arr[i] == 'Slider':
                sl_ext_sum += float(self.ext_arr[i])
                sl_qt += 1
        if sl_qt > 0:
            self.avg_ext_sl = round(sl_ext_sum / sl_qt, 2)
        else:
            self.avg_ext_sl = "* No slider extension measurements taken this session *"

    def get_avg_che(self):
        ch_ext_sum = 0.0
        ch_qt = 0
        for i in range(len(self.ext_arr)):
            if self.ext_arr[i] != '--' and self.pitch_type_arr[i] == 'Changeup':
                ch_ext_sum += float(self.ext_arr[i])
                ch_qt += 1
        if ch_qt > 0:
            self.avg_ext_ch = round(ch_ext_sum / ch_qt, 2)
        else:
            self.avg_ext_ch = "* No changeup extension measurements taken this session *"

    def gen_avg_vals(self):
        self.get_avg_fbv()
        self.get_avg_cbv()
        self.get_avg_slv()
        self.get_avg_chv()
        self.get_avg_fbs()
        self.get_avg_cbs()
        self.get_avg_sls()
        self.get_avg_chs()
        self.get_avg_fbe()
        self.get_avg_cbe()
        self.get_avg_sle()
        self.get_avg_che()


def main():
    player = Player()
    player.generate_arrays()
    player.gen_avg_vals()
    print("\nName: " + player.player_name)
    print("\n### AVG. VELO STATS ###")
    print("Avg FB velo: " + str(player.avg_fb_vel) + " mph")
    print("Avg SL velo: " + str(player.avg_sl_vel) + " mph")
    print("Avg CB velo: " + str(player.avg_cb_vel) + " mph")
    print("Avg CH velo: " + str(player.avg_ch_vel) + " mph")
    print("\n### SPIN RATE STATS ###")
    print("Avg FB spin rate: " + str(player.avg_fb_spin) + " rpm")
    print("Avg SL spin rate: " + str(player.avg_sl_spin) + " rpm")
    print("Avg CB spin rate: " + str(player.avg_cb_spin) + " rpm")
    print("Avg CH spin rate: " + str(player.avg_ch_spin) + " rpm")
    print("\n### EXTENSION STATS ###")
    print("Avg FB spin rate: " + str(player.avg_ext_fb) + " ft")
    print("Avg SL spin rate: " + str(player.avg_ext_sl) + " ft")
    print("Avg CB spin rate: " + str(player.avg_ext_cb) + " ft")
    print("Avg CH spin rate: " + str(player.avg_ext_ch) + " ft")


if __name__ == '__main__':
    main()

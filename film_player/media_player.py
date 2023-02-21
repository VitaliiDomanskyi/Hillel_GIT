class Player:
    def __init__(self, media, quality='720p'):
        self.media = media
        self.quality = quality
        self.playing = False
        self.current_time = 0

    def play(self, file_path):
        if self.playing:
            print("Медіа вже відтворюється.")
            return False
        else:
            try:
                with open(file_path, 'r') as file:
                    self.playing = True
                    print(f"Відтворюється {self.media} у якості {self.quality}.")
                    return True
            except:
                print(f"Помилка відкриття файлу {file_path}")
                return False

    def pause(self):
        if self.playing:
            self.playing = False
            print(f"Пауза {self.media} на {self.current_time} секунді.")
        else:
            print("Медіа зараз не відтворюється")

    def save_last_time(self, current_time):
        self.current_time = current_time
        print(f"Збережено {self.media} на {self.current_time} секунді.")

    def change_quality(self, new_quality):
        self.quality = new_quality
        print(f"Змінено якість з {self.media} на {self.quality}.")

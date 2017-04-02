from tweepy.streaming import StreamListener

class AlertsListener(StreamListener):

    def on_data(self, data):
        try:
            with open('disasterAlerts.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print('Error on_data:' + str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

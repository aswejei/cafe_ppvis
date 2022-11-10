from python.extension2.ApplicationExt2 import ApplicationExt2

if __name__ == '__main__':
    model = ApplicationExt2.build()
    print('Start modelling')
    model.run()
    print(f'Finish rating: {model.getAvgRating()}')

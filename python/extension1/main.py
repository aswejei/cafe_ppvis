from python.extension1.ApplicationExt1 import ApplicationExt1

if __name__ == '__main__':
    model = ApplicationExt1.build()
    print('Start modelling')
    model.run()
    print(f'Finish rating: {model.getAvgRating()}')

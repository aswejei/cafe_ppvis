from extension4.ApplicationExt4 import ApplicationExt4

if __name__ == '__main__':
    model = ApplicationExt4.build()
    print('Start modelling')
    model.run()
    print(f'Finish rating: {model.getAvgRating()}')
    model.printMoreStatistics()
from extension3.ApplicationExt3 import ApplicationExt3

if __name__ == '__main__':
    model = ApplicationExt3.build()
    print('Start modelling')
    model.run()
    print(f'Finish rating: {model.getAvgRating()}')

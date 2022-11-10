from python.extension5.ApplicationExt5 import ApplicationExt5

if __name__ == '__main__':
    model = ApplicationExt5.build()
    print('Start modelling')
    model.run()
    print(f'Finish rating: {model.getAvgRating()}')
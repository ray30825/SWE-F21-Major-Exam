import pandas as pd, seaborn as sns, numpy as np, matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')
# set seed for reproducibility
np.random.seed(0)
service_type = int(input('Please Select the service: 1.Banks 2.Packet switching router'))

if service_type == 1:
    l = int(input('Please enter the average customers per minute：'))
    µ = float(input('Please enter the average number of people served per minute：'))
    ncust = int(input('Please enter the number of customers：'))
    c = 1  # number of servers
    utilization = {}
    service_times = []  # list of service times once they reach the front

    # generating inter arrival times using exponential distribution
    while c <= 2:
        if c == 1:
            inter_arrival_times = list(np.random.exponential(scale=1 / l, size=ncust))

        arrival_times = []  # list of arrival times of a person joining the queue
        finish_times = []  # list of finish times after waiting and being served

        arrival_times = [0 for i in range(ncust)]
        finish_times = [0 for i in range(ncust)]

        arrival_times[0] = round(inter_arrival_times[0], 4)  # arrival of first customer

        # Generate arrival times

        for i in range(1, ncust):
            arrival_times[i] = round((arrival_times[i - 1] + inter_arrival_times[i]), 4)

            # Generate random service times for each customer
        if c == 1:
            service_times = list(np.random.exponential(scale=1 / µ, size=ncust))

            # Generate finish times
        finish_times[0] = round((arrival_times[0] + service_times[0]), 4)
        for i in range(1, ncust):
            previous_finish = finish_times[:i]
            previous_finish.sort(reverse=True)
            previous_finish = previous_finish[:c]
            if i < c:
                finish_times[i] = round(arrival_times[i] + service_times[i], 4)
            else:
                finish_times[i] = round((max(arrival_times[i], min(previous_finish)) + service_times[i]), 4)

            # Total time spent in the system by each customer
        total_times = [abs(round((finish_times[i] - arrival_times[i]), 4)) for i in range(ncust)]

        # Time spent@waiting before being served (time spent in the queue)
        wait_times = [abs(round((total_times[i] - service_times[i]), 4)) for i in range(ncust)]

        # creating a dataframe with all the data of the model
        data = pd.DataFrame(
            list(zip(arrival_times, finish_times, service_times, total_times, wait_times, inter_arrival_times)),
            columns=['arrival_times', 'finish_times', 'service_times', 'total_times', 'wait_times',
                     'inter_arrival_times'])

        # generating the timeline , and their description (arrivals, departures)

        tbe = list([0])
        timeline = ['simulation starts']
        for i in range(0, ncust):
            tbe.append(data['arrival_times'][i])
            tbe.append(data['finish_times'][i])
            timeline.append('customer ' + str(i + 1) + ' arrived')
            timeline.append('customer ' + str(i + 1) + ' left')

        # generating a dataframe with the timeline and description of events

        timeline = pd.DataFrame(list(zip(tbe, timeline)),
                                columns=['time', 'Timeline']).sort_values(by='time').reset_index()
        timeline = timeline.drop(columns='index')

        # generating the number of customers inside the system at any given time of the simulation
        # and recording idle and working times

        timeline['n'] = 0
        x = 0
        for i in range(1, (2 * ncust) - 1):
            if len(((timeline.Timeline[i]).split())) > 2:
                z = str(timeline['Timeline'][i]).split()[2]
            else:
                continue
            if z == 'arrived':
                x = x + 1
                timeline['n'][i] = x
            else:
                x = x - 1
                if x == -1:
                    x = 0
                timeline['n'][i] = x

        # computing time between events
        t = list()
        for i in timeline.index:
            if i == (2 * ncust) - 2:
                continue
            if i < 2 * ncust:
                x = timeline.time[i + 1]
            else:
                x = timeline.time[i]
            y = timeline.time[i]
            t.append(round((x - y), 4))

        t.append(0)
        timeline['tbe'] = t

        # computing the probability of 'n' customers being in the system

        Pn = timeline.groupby('n').tbe.agg(sum) / sum(t)
        Tn = timeline.groupby('n').tbe.agg('count')

        # checking central tendency measures and dispersion of the data
        timeline.n.describe()

        # computing expected number of customers in the system
        Ls = (sum(Pn * Pn.index))

        # computing expected customers waiting in line
        Lq = sum((Pn.index[c + 1:] - 1) * (Pn[c + 1:]))

        # plots

        plt.figure(figsize=(12, 4))
        sns.lineplot(x=data.index, y=wait_times, color='black').set(xticklabels=[])
        plt.xlabel('Customer number')
        plt.ylabel('minutes')
        plt.title('Wait time of customers with ' + str(c) + ' servers')
        sns.despine()
        plt.show()

        utilization.setdefault(c, (Ls - Lq) / c)

        print('Output:', '\n',
              'Servers : ' + str(c), '\n '
                                     'Time Between Arrivals : ', str(data.inter_arrival_times.mean()), '\n',
              'Service Time: (1/µ)', str(data.service_times.mean()), '\n'
                                                                     ' Utilization (c): ', str((Ls - Lq) / c), '\n',
              'Expected wait time in line (minute):', str(data['wait_times'].mean()), '\n',
              'Expected time spent on the system (minute):', str(data.total_times.mean()), '\n',
              'Expected number of customers in line (Lq):', str(Lq), '\n',
              'Expected number of clients in the system (Ls):', str(Ls), '\n '
                                                                         'Expected number of occupied servers :',
              str(Ls - Lq), '\n')

        c = c + 1

    utilization = pd.Series(utilization)
    plt.figure(figsize=(6, 6))
    sns.pointplot(x=utilization.index, y=utilization)
    plt.xlabel('Number of servers')
    plt.ylabel('Utilization')
    plt.title('number of servers vs Utilization')

if service_type == 2:
    l = int(input('Please enter the average packet per minute：'))  # average number of arrivals per minute
    µ = float(input('Please enter the average number of packet departed per minute：'))
    ncust = int(input('Please enter the number of packets：'))
    c = 1  # number of servers
    utilization = {}
    service_times = []  # list of service times once they reach the front

    # generating inter arrival times using exponential distribution
    while c <= 2:
        if c == 1:
            inter_arrival_times = list(np.random.exponential(scale=1 / l, size=ncust))

        arrival_times = []  # list of arrival times of a person joining the queue
        finish_times = []  # list of finish times after waiting and being served

        arrival_times = [0 for i in range(ncust)]
        finish_times = [0 for i in range(ncust)]

        arrival_times[0] = round(inter_arrival_times[0], 4)  # arrival of first customer

        # Generate arrival times

        for i in range(1, ncust):
            arrival_times[i] = round((arrival_times[i - 1] + inter_arrival_times[i]), 4)

            # Generate random service times for each customer
        if c == 1:
            service_times = list(np.random.exponential(scale=1 / µ, size=ncust))

            # Generate finish times
        finish_times[0] = round((arrival_times[0] + service_times[0]), 4)
        for i in range(1, ncust):
            previous_finish = finish_times[:i]
            previous_finish.sort(reverse=True)
            previous_finish = previous_finish[:c]
            if i < c:
                finish_times[i] = round(arrival_times[i] + service_times[i], 4)
            else:
                finish_times[i] = round((max(arrival_times[i], min(previous_finish)) + service_times[i]), 4)

            # Total time spent in the system by each customer
        total_times = [abs(round((finish_times[i] - arrival_times[i]), 4)) for i in range(ncust)]

        # Time spent@waiting before being served (time spent in the queue)
        wait_times = [abs(round((total_times[i] - service_times[i]), 4)) for i in range(ncust)]

        # creating a dataframe with all the data of the model
        data = pd.DataFrame(
            list(zip(arrival_times, finish_times, service_times, total_times, wait_times, inter_arrival_times)),
            columns=['arrival_times', 'finish_times', 'service_times', 'total_times', 'wait_times',
                     'inter_arrival_times'])

        # generating the timeline , and their description (arrivals, departures)

        tbe = list([0])
        timeline = ['simulation starts']
        for i in range(0, ncust):
            tbe.append(data['arrival_times'][i])
            tbe.append(data['finish_times'][i])
            timeline.append('customer ' + str(i + 1) + ' arrived')
            timeline.append('customer ' + str(i + 1) + ' left')

        # generating a dataframe with the timeline and description of events

        timeline = pd.DataFrame(list(zip(tbe, timeline)),
                                columns=['time', 'Timeline']).sort_values(by='time').reset_index()
        timeline = timeline.drop(columns='index')

        # generating the number of customers inside the system at any given time of the simulation
        # and recording idle and working times

        timeline['n'] = 0
        x = 0
        for i in range(1, (2 * ncust) - 1):
            if len(((timeline.Timeline[i]).split())) > 2:
                z = str(timeline['Timeline'][i]).split()[2]
            else:
                continue
            if z == 'arrived':
                x = x + 1
                timeline['n'][i] = x
            else:
                x = x - 1
                if x == -1:
                    x = 0
                timeline['n'][i] = x

        # computing time between events
        t = list()
        for i in timeline.index:
            if i == (2 * ncust) - 2:
                continue
            if i < 2 * ncust:
                x = timeline.time[i + 1]
            else:
                x = timeline.time[i]
            y = timeline.time[i]
            t.append(round((x - y), 4))

        t.append(0)
        timeline['tbe'] = t

        # computing the probability of 'n' customers being in the system

        Pn = timeline.groupby('n').tbe.agg(sum) / sum(t)
        Tn = timeline.groupby('n').tbe.agg('count')

        # checking central tendency measures and dispersion of the data
        timeline.n.describe()

        # computing expected number of customers in the system
        Ls = (sum(Pn * Pn.index))

        # computing expected customers waiting in line
        Lq = sum((Pn.index[c + 1:] - 1) * (Pn[c + 1:]))

        # plots

        plt.figure(figsize=(12, 4))
        sns.lineplot(x=data.index, y=wait_times, color='black').set(xticklabels=[])
        plt.xlabel('Packet number')
        plt.ylabel('minutes')
        plt.title('Wait time of Packet with ' + str(c) + ' servers')
        sns.despine()
        plt.show()

        utilization.setdefault(c, (Ls - Lq) / c)

        print('Output:', '\n',
              'Servers : ' + str(c), '\n '
                                     'Time Between Arrivals : ', str(data.inter_arrival_times.mean()), '\n',
              'Service Time: (1/µ)', str(data.service_times.mean()), '\n'
                                                                     ' Utilization (c): ', str((Ls - Lq) / c), '\n',
              'Expected wait time in line (minute):', str(data['wait_times'].mean()), '\n',
              'Expected time spent on the system (minute):', str(data.total_times.mean()), '\n',
              'Expected number of customers in line (Lq):', str(Lq), '\n',
              'Expected number of clients in the system (Ls):', str(Ls), '\n '
                                                                         'Expected number of occupied servers :',
              str(Ls - Lq), '\n')

        c = c + 1

    utilization = pd.Series(utilization)
    plt.figure(figsize=(6, 6))
    sns.pointplot(x=utilization.index, y=utilization)
    plt.xlabel('Number of servers')
    plt.ylabel('Utilization')
    plt.title('number of servers vs Utilization')

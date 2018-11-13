figure(1);
y1=[44.64 48.21 43.87 76.33 3.57];
x1=[1 2 3 4 5];
plot(x1,y1,'r-o');
hold on;
y1=[53.57 50.0 53.58 52.67 51.19];
x1=[1 2 3 4 5];
plot(x1,y1,'b-x');
legend('Vanilla RR(Independent)','Multitasl Learning');
title('Comparison: Independent v/s Multitask Learning');
ylabel('Accuracy(%)');
xlabel('Subjects');
grid on;



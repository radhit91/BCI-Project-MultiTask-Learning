figure(1);
y1=[53.57 62.5 48.47 48.21 51.19];
x1=[1 2 3 4 5];
plot(x1,y1,'r-o');
hold on;
y1=[54.46 50.0 51.3 45.08 49.60];
x1=[1 2 3 4 5];
plot(x1,y1,'g-x');
hold on;
y1=[55.35 50.4 53.59 47.32 49.60];
x1=[1 2 3 4 5];
plot(x1,y1,'b-*');
hold on;
y1=[50.89 57.14 56.12 52.67 50.79];
x1=[1 2 3 4 5];
plot(x1,y1,'k-+');
hold on;
y1=[52.69 58.92 53.06 49.10 51.19];
x1=[1 2 3 4 5];
plot(x1,y1,'y-^');


legend('Multitask Learning(Subject-1)','Multitask Learning(Subject-2)','Multitask Learning(Subject-3)','Multitask Learning(Subject-4)','Multitask Learning(Subject-5)');
title('Comparison: Multitask Learning across subjects');
ylabel('Accuracy(%)');
xlabel('Subjects');
grid on;





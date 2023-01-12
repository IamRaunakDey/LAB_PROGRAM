#include<stdio.h>
#include<math.h>
void division(int arr[],int val){
    int key;
    key = val%10;
    if (arr[key]==-1){
        arr[key] = val;
    }
    else{
        printf("\n Collision occurred");
        return;
    }

}
void display(int arr[]){
    for(int i=0;i<10;i++){
        if(arr[i]==-1)
        printf("_ ");
        else 
        printf("%d ",arr[i]);
    }
}
void multi(int arr[],int val){
    int key;
    double t,val1,i;
    val1=val;
    t = 0.618033*val1;
    double k;
    k = modf(t,&i);
    key = floor(10*k);
    if (arr[key]==-1){
        arr[key] = val;
    }
    else{
        printf("\n Collision occurred");
        return;
    }

}
void ms(int arr[],int val){
    int sq;
    sq=val*val;
    int i,c,no[50];
    i=0;
    int tk;
    while(sq!=0){
        c=sq%10;
        sq=sq/10;
        no[i]=c;
        i++;
    }
    tk=i/2;
    int pos;
    pos = no[tk];
    if(arr[pos]==-1){
        arr[pos]=val;
        return;
    }
    printf("\n Collision occured");
}
void linprob(int arr[],int val){
    int i,key,flag,k2;
    i=0;
    flag=0;
    key=val%10;
    while(i!=10){
    k2=(key+i)%10;
    if(arr[k2]==-1){
        arr[k2]=val;
        flag=1;
        return;
    }
    i=i+1;
   }
    
    if(flag==0){
        printf("\n No space found to insert element . Hash table is full.");
    }
}
void fold(int arr[],int val){
    int sum;
    int t,v,pos;
    v=val;
    while(v!=0){
        t=v%10;
        v=v/10;
        sum+=t;
    }
    pos=sum%10;
    if(arr[pos]==-1){
        arr[pos]=val;
        return;
    }
    printf("\n Collision Occured");
}
void main(){
    int arr[10],val;
    for(int i=0;i<10;i++){
        arr[i]=-1;
    }
    int ch;
    while(ch!=7){

        printf("\n1.DIVISION\n2.MULTIPLICATION\n3.MID SQUARE\n4.FOLDING\n5.Linear probing\n6.DISPLAY\n7.EXIT\n");
        printf("\n Enter your choice: ");
        scanf("%d",&ch);
        
        switch(ch){
            case 1:
                printf("\n Enter value to be inserted : ");
                scanf("%d",&val);
                division(arr,val);
                break;
            case 2:
                printf("\n Enter value to be inserted : ");
                scanf("%d",&val);
                multi(arr,val);
                break;
            case 3:
                printf("\n Enter value to be inserted : ");
                scanf("%d",&val);
                ms(arr,val);
                break;
            case 4:
                printf("\n Enter value to be inserted : ");
                scanf("%d",&val);
                fold(arr,val);
                break;
            case 5:
                printf("\n Enter value to be inserted : ");
                scanf("%d",&val);
                linprob(arr,val);
                break;
            case 6:
                display(arr);
                break;
            case 7:
                break;
        }
    }
}
#include <stdio.h>

int main()
{

	int a[10];//배열 크기정의

	printf("===== 메뉴 =====\nPUSH = 1 \n POP = 2 \nSHOW = 3\n(종료하려면 1,2,3외의 숫자입력)\n");
	int i = 0;
	int k;
	
	while(1)//무한루프
	{
		printf("메뉴를 입력하시오 : ");//메뉴를 입력받는다
		scanf_s("%d", &k);
		
		switch (k)
		{
		case 1://k가1이라면 배열에 수를 입력하고 그다음 배열칸을 만든다
			printf("수 입력 : ");
			scanf_s("%d", &a[i]);
			i++;			
			break;
		
		case 2://k가2라면 만들었던배열을 삭제한다
			i--;
			break;
		
		case 3://k가3이라면 여태껏 저장되있던 배열을 출력한다
			for (int num = 0; num < i; num++)
			{
				printf("%d ", a[num]);
			}
			
			break;

		default://그외의 숫자를 입력하게되면 루프를 멈춘다
			
			return 0;
			break;

		}
	}

}

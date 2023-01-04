/*
{   전처리기 X, 바로 메인함수
    연산시 casting

}*/

#[allow(unused_variables)] // 사용하지 않은 변수 경고x vscode

//function
fn op(n1:i32,n2:i32) ->i32{ //->return 자료형 선언

    n1*n2 //return ;X
}

fn printOp(n1:i32,n2:i32){ //return x 함수
    let result: i32=n1*n2;
    println!("{n1}*{n2}={result}");
}

fn mul_ten(n:i32){
    let number={ //코드블럭 ==익명함수
    let ten=10;
    n*ten
};
    println!("{number}");
}

fn main() {
//int (let 변수명 :i비트=값; let 변수명:값_i비트;)
    let num:i8=10; //int 8bit == short num=10;, 쓰지 않음 _변수명
    let num2 =20_i16;
    let num3=30; // default=i16
    let num4= num3+num2; //같은 비트수의 자료형끼리
    let num5=num+num2 as i8; //자료형 맞추기 ==casting , 더 작은 비트수로

    println!("{}={}+{}",num4,num2,num3);
    println!("{o}={t}+{th}",o=num4,t=num2,th=num3);
    println!("{num4}={num2}+{num3}");
    println!("{num5}={num}+{num2}");

    let a=3;
    let b=4;
    let c=op(a,b);
    println!("{a}*{b}={c}");
    
    printOp(3,4); //empty tuple() 변수 저장 X
    mul_ten(a);


//float 
    let num: f32=10.1;
    let num2 = 20_f64;
    let num3 =30.3;

//char '', string ""
    let aa= 'a'; //char
    let bb="word"; //string
    let space = " "; //space ==NULL포함
    let emoji = " ";

//print!
    print!("hi");// ! macro 출력 타입 축약, escape O
    println!("
    d
    d
    d "); //line 인식
}
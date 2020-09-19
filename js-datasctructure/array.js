class CustomArray{

    constructor(){
        this.data = {};
        this.length = 0;
    }

    get(index){
        this.view();
        return this.data[index];
    }

    push(item){        
        this.data[this.length] = item;
        this.length++;
        this.view();
        return this.data;
    }

    pop(){
        delete this.data[this.length -1];
        this.length--;
        this.view();
    }

    delete(index){
        console.log(this.data[index]);
        delete this.data[index];
        this.shiftIndex(index);
        return this.data[index];
    }

    shiftIndex(index){
        for(let i=index; i<this.length; i++){
            this.data[i] = this.data[i+1];
        }
        delete this.data[this.length-1];
        this.length--;
        this.view();
    }

    view(){
        console.log(this.data);
    }

}

const Arr = new CustomArray();
Arr.push("Hi");
Arr.push("How");
Arr.push("Are");
Arr.push("you");
Arr.push("?");
//Arr.get(3);
// Arr.pop();
// Arr.pop();
// Arr.pop();
Arr.delete(2);

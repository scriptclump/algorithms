class CustomString{

    constructor(){

    }

    reverse(str){
        // Validation
        if(!str){
            return false;
        }
        let rev_str = '';
        for(let i=str.length -1; i >=0; i--){
            rev_str += str[i];
        }
        console.log(rev_str);
        return rev_str;
    }
}

const cs = new CustomString();
cs.reverse('test');
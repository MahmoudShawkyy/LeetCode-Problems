//after increasing, reset temp = "" (empty string).
temp = "";
}
}
}
//the following if case if when the paragraph ends without a fullstop.
if(temp!=""){
transform(temp.begin(),temp.end(),temp.begin(),::tolower);
arr[temp]++;
}
//now we iterate through the banned vector to see if have counted those words in the map. If yes, we delete that element from map.
for(int i=0;i<ban.size();i++){
if(arr.find(ban[i])!=arr.end()){
arr.erase(ban[i]);
}
}
//Now we will find the most frequent word
string word;
int count = INT_MIN;
for(auto i:arr){
if(i.second>count){
count = i.second;
word = i.first;
}
}
return word;
}
};
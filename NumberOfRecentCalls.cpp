class RecentCounter {
private:
    vector<int> que;

public:
    RecentCounter() {
    }
    
    int ping(int t) {
        que.push_back(t);

        while(que.front() < t-3000){
            que.erase(que.begin());
        }
        return que.size();
    }
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
 */
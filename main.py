#include "CAL.h"
int main(int argc, char* argv[]) {
    if (argc < 3) return 0;
        string filename = string(argv[1]);
        ifstream file;
        file.open(filename);
        if (!file.good()) {
            cout << "File '" << filename << "' could not be opened." << endl;
            return 0;
            }
        int DLLsize = argv[2];
    createMap(file, DLLsize);
return 0;
}


void createMap(std::string temp, std::ofstream &ofs, LinkedList<T>* LLptr) {

}

string toString(){
    
}

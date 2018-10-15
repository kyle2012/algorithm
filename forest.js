class Analysis {

  static initialize(num, relations) {
    return new Analysis(num, relations);
  }

  constructor(num, relations) {
    this.members = Array(num+1).fill(-1);
    this.relations = relations;
  }

  calculate() {
    for(let i=0; i<this.relations.length; i++){
      this.mergeTree(this.relations[i][0], this.relations[i][1])
    }
    console.log(this.members);
  }

  getRoot(node) {
    while(this.members[node] >= 0) {
      node = this.members[node];
    }
    return node;
  }

  mergeTree(node1, node2) {
    let root1 = this.getRoot(node1)
    let root2 = this.getRoot(node2)
    if(root1 != root2) {
      this.members[root1] = this.members[root1] + this.members[root2];
      this.members[root2] = root1;
    }
  }

}
Analysis.initialize(5, [[1,2],[2,3],[4,5]]).calculate()

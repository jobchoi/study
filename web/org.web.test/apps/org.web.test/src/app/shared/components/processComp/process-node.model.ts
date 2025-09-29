export interface Queue<T>{
  items:T[]

  enqueue(item:T):void
  dequeue():T|null
  isempty():boolean

  peek():T|null
}

export interface Item{
  id:string
  type: string
  history:string[]
  status:'waiting'|'processing'|'error'|'done'
  createAt:number
  currentTick:number
}
export interface Machine{
  id :string
  speed:number
  errorRate : number
  currentItem : Item | null
  progress:number
  
}

export interface ProcessNode {
  id: number;
  name: string;
  x: number;
  y: number;
  w: number;
  next: number[];
}


export interface ProcessNod {
  id: string                // 공정 이름 (e.g., "가공1")
  machine: Machine          // 연결된 기계 정보
  inputQueue: Queue<Item>   // 대기 중인 작업 아이템
  outputQueue: Queue<Item>  // 처리 완료 후 대기
  nextSteps: string[]       // 다음으로 이동할 노드 id 목록
}

export interface Machine{
  id: string
  speed: number             // 처리 속도 (item/tick)
  errorRate: number         // 실패 확률 (%)
  currentItem: Item | null  // 현재 처리 중인 아이템
  progress: number          // 처리 진행도

}
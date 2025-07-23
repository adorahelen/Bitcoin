# Bitcoin
블록체인 개발 및 포렌식 공부

-----


#### 1\. VSCode 설치 및 프로젝트 시작

  * **Visual Studio Code (VSCode)** 설치
  * 터미널에서 프로젝트 디렉토리 생성 및 이동:
    ```bash
    mkdir blockchain && cd blockchain
    ```

#### 2\. Node.js 설치

  * 최신 LTS 버전의 **Node.js** 설치
  * 설치 확인:
    ```bash
    node -v
    npm -v
    ```

#### 3\. Hardhat 프로젝트 초기화

  * **Hardhat** 설치:
    ```bash
    npm install --save-dev hardhat
    ```
  * **Hardhat** 프로젝트 생성:
    ```bash
    npx hardhat
    ```
  * `Create a JavaScript project` 선택 후 기본 설정으로 생성

#### 4\. ERC-20 토큰 스마트 컨트랙트 작성

  * `contracts/MyToken.sol` 파일 생성 및 아래 내용 작성:
    ```solidity
    // SPDX-License-Identifier: MIT
    pragma solidity ^0.8.0;

    import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

    contract MyToken is ERC20 {
        constructor(uint256 initialSupply) ERC20("MyToken", "MTK") {
            _mint(msg.sender, initialSupply);
        }
    }
    ```
  * **OpenZeppelin** 설치:
    ```bash
    npm install @openzeppelin/contracts
    ```

#### 5\. 배포 스크립트 작성

  * `scripts/deploy.js` 파일 생성 및 아래 내용 작성:
    ```javascript
    async function main() {
      const MyToken = await ethers.getContractFactory("MyToken");
      const myToken = await MyToken.deploy(ethers.utils.parseUnits("1000", 18));
      await myToken.waitForDeployment();

      console.log("MyToken deployed to:", await myToken.getAddress());
    }

    main().catch((error) => {
      console.error("❌ 배포 오류:", error);
      process.exitCode = 1;
    });
    ```

#### 6\. 하드햇 로컬 노드 실행

  * 새 터미널에서 실행:
    ```bash
    npx hardhat node
    ```
      * 가짜 계정 20개 생성
      * 로컬 블록체인 실행 중 (`http://127.0.0.1:8545`)

#### 7\. 배포 실행

  * 기존 터미널에서 배포:
    ```bash
    npx hardhat run scripts/deploy.js --network localhost
    ```
  * **결과 (예시):**
    ```
    MyToken deployed to: 0x12321312sadaassad2421412
    ```

#### 8\. 오류 디버깅

  * **배포 중 발생한 오류:** `❌ 배포 오류: TypeError: myToken.deployed is not a function`
  * **해결:** `deployed()` 함수는 하드햇에서 비동기 배포 방식이 변경되어 제거됨. `waitForDeployment()`로 수정.

-----

### 🔜 다음 단계 (프론트엔드 연동)

이제 로컬에 배포된 **MyToken** 컨트랙트를 프론트엔드(`HTML`, `JavaScript`, `Ethers.js` 등)에서 연결해 토큰 전송 기능을 구현할 수 있습니다.

다음 단계는 다음과 같습니다:

1.  `frontend` 폴더 만들기
2.  **메타마스크**에 하드햇 로컬 노드 연결
3.  **Ethers.js**를 이용해 사용자 지갑 연결
4.  프론트엔드에서 토큰 전송 기능 구현

# Feature Flags Service

테넌트별 기능 플래그 조회를 제공하는 작은 Python 서비스 라이브러리입니다.

이 저장소는 Clio Benchmark에서 분석 대상으로 사용하는 테스트 fixture입니다. 프로덕션 용도로 사용하지 않습니다.

## 실행

```shell
uv sync --extra dev
uv run pytest
```

## 구조

- `src/feature_flags/repository.py`: 테넌트별 플래그 저장소
- `src/feature_flags/cache.py`: 조회 결과 캐시
- `src/feature_flags/service.py`: 플래그 조회 서비스
- `src/feature_flags/authorization.py`: 관리자 권한과 프로젝트 범위 검사
- `src/feature_flags/rollout.py`: percentage rollout 계산
- `src/feature_flags/targeting.py`: 국가·사용자 타기팅
- `benchmark.json`: Clio에 전달할 버그 리포트

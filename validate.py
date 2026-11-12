#!/usr/bin/env python3
"""Run repeatable checks over a device-validation JSON fixture."""
import argparse,json,time
from datetime import datetime,timezone
from pathlib import Path

def run(plan, fixture):
 results=[]
 for case in plan:
  started=time.perf_counter(); name=case["name"]; path=case["path"].split("."); value=fixture
  try:
   for part in path:value=value[int(part)] if isinstance(value,list) else value[part]
   op=case.get("op","equals"); expected=case.get("expected")
   if op=="equals":passed=value==expected
   elif op=="contains":passed=expected in value
   elif op=="truthy":passed=bool(value)
   elif op=="type":passed=type(value).__name__==expected
   else:raise ValueError(f"unsupported operation: {op}")
   reason="passed" if passed else f"actual {value!r} did not satisfy {op} {expected!r}"
  except (KeyError,IndexError,TypeError,ValueError) as e:passed=False;reason=str(e)
  results.append({"name":name,"passed":passed,"reason":reason,"duration_ms":round((time.perf_counter()-started)*1000,3)})
 return {"created_at":datetime.now(timezone.utc).isoformat(),"passed":sum(r["passed"] for r in results),"failed":sum(not r["passed"] for r in results),"results":results}
def main():
 p=argparse.ArgumentParser();p.add_argument("plan",type=Path);p.add_argument("fixture",type=Path);p.add_argument("--output",type=Path,default=Path("validation-report.json"));a=p.parse_args()
 report=run(json.loads(a.plan.read_text()),json.loads(a.fixture.read_text()));a.output.write_text(json.dumps(report,indent=2)+"\n");print(f"{report['passed']} passed, {report['failed']} failed");raise SystemExit(1 if report["failed"] else 0)
if __name__=="__main__":main()

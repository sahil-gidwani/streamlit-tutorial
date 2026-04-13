# Module 4: Expected Goals (xG) Lab

## Learning Goals
- Build a simple xG model demo with logistic regression
- Explain model input features and limitations
- Visualize shot probability intuitively for non-technical viewers

## Build
Run:
```bash
streamlit run apps/04_xg_lab.py
```

## Modeling Scope
This tutorial intentionally uses a lightweight model for explainability.

Feature set:
- Shot distance
- Shot angle
- Body part (foot/head)
- Open play vs set piece

Target:
- `is_goal` (0/1)

## Example Snippet: Train Model
```python
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression

pre = ColumnTransformer([
    ("num", StandardScaler(), ["distance", "angle"]),
    ("cat", OneHotEncoder(handle_unknown="ignore"), ["body_part", "play_type"]),
])

model = Pipeline([
    ("pre", pre),
    ("clf", LogisticRegression(max_iter=1000)),
])
```

## Explainability Segment for Demos
- Distance generally has a negative effect on goal probability.
- Central shooting angles generally increase probability.
- Headers usually have different baseline conversion rates than shots with feet.

## Practice Tasks
1. Add calibration plot by predicted probability bucket.
2. Add feature impact summary with model coefficients.
3. Add a shot simulator panel where user controls distance and angle.
4. Compare model xG totals vs actual goals by match.

## Important Caveats
- This is not a production xG model.
- Event provider definitions differ.
- Shot context (pressure, defensive shape) is mostly absent in simple demos.

## Next Module
Go to [05-multipage-football-app.md](./05-multipage-football-app.md).

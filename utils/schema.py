import polars as pl

schema_map = {

    # --------------------------------
    # players.csv
    # --------------------------------
    "players": {
        "nfl_id": pl.Int64,
        "display_name": pl.String,
        "draft_year": pl.Int64,
        "nfl_position": pl.String,
        "birth_date": pl.String,
        "college_name": pl.String,
        "college_conference": pl.String,
        "draft_round": pl.String,
        "draft_pick_within_round": pl.Int64,
        "draft_overall_pick": pl.Int64
    },

    # --------------------------------
    # combine_results.csv
    # --------------------------------
    "combine_results": {
        "draft_year": pl.Int64,
        "nfl_id": pl.Int64,
        "combine_position": pl.String,
        "combine_height": pl.Float64,
        "combine_weight": pl.Int64,
        "hand_size": pl.Float64,
        "arm_length": pl.Float64,
        "wing_span": pl.Float64,
        "ten_yd_split": pl.Float64,
        "forty": pl.Float64,
        "vertical": pl.Float64,
        "broad_jump": pl.Int64,
        "three_cone": pl.Float64,
        "short_shuttle": pl.Float64,
        "bench_reps": pl.Int64,
        "ngs_athleticism_score": pl.Int64,
        "ngs_college_production_score": pl.Float64,
        "ngs_final_score": pl.Float64,
    },

    # -------------------------------
    # combine_tracking.csv
    # -------------------------------
    "combine_tracking": {
        "draft_year": pl.Int64,
        "event_id": pl.String,
        "nfl_id": pl.Int64,
        "entity_type": pl.String,
        "time": pl.Datetime,
        "drill_type": pl.String,
        "drill_name": pl.String,
        "attempt": pl.Int64,
        "x": pl.Float64,
        "y": pl.Float64,
        "s": pl.Float64,
        "a": pl.Float64,
        "dis": pl.Float64,
        "dir": pl.Float64,
    },

    # ------------------------------
    # player_career_successes.csv
    # ------------------------------
    "player_career_successes": {
        "nfl_id": pl.Int64,
        "career_offensive_snaps": pl.Int64,
        "career_defensive_snaps": pl.Int64,
        "career_special_teams_snaps": pl.Int64,
        "career_games_active": pl.Int64,
        "career_games_started": pl.Int64,
        "ap_all_pro_1st_team": pl.Int64,
        "ap_all_pro_2nd_team": pl.Int64,
        "pro_bowl_original_ballot": pl.Int64,
    },

    # -----------------------------
    # player_play.csv
    # -----------------------------
    "player_play": {
        "game_id": pl.Int64,
        "play_id": pl.Int64,
        "team_abbr": pl.String,
        "nfl_id": pl.Int64,
        "lined_up_position": pl.String,
        "play_description": pl.String,
        "quarter": pl.Int64,
        "down": pl.Int64,
        "yards_to_go": pl.Int64,
        "possession_team": pl.String,
        "yardline_side": pl.String,
        "yardline_number": pl.Int64,
        "game_clock": pl.String,
        "pre_snap_home_score": pl.Int64,
        "pre_snap_visitor_score": pl.Int64,
        "play_direction": pl.String,
        "pre_snap_home_team_win_probability": pl.Float64,
        "pre_snap_visitor_team_win_probability": pl.Float64,
        "home_team_win_probability_added": pl.Float64,
        "visitor_team_win_probability_added": pl.Float64,
        "expected_points_added": pl.Float64,
        "expected_points": pl.Float64,
        "offense_formation": pl.String,
        "receiver_alignment": pl.String,
        "pass_result": pl.String,
        "pass_length": pl.Float64,
        "play_nullified_by_penalty": pl.Boolean,
        "penalty_yards": pl.Float64,
        "pre_penalty_yards_gained": pl.Int64,
        "yards_gained": pl.Int64,
        "team_coverage_man_zone": pl.String,
        "team_coverage_type": pl.String,
        "in_motion_at_ball_snap": pl.Boolean,
        "target": pl.Boolean,
        "rec_yards": pl.Float64,
        "rush_yards": pl.Float64,
        "yards_after_catch": pl.Float64,
        "fumble": pl.Boolean,
        "fumble_lost": pl.Boolean,
        "route_ran": pl.String,
        "separation_at_pass_forward": pl.Float64,
        "cushion": pl.Float64,
        "expected_yards_after_catch": pl.Float64,
        "dropback_duration": pl.Float64,
        "extended_sack_allowed": pl.Float64,
        "pass_rushers_encountered": pl.Float64,
        "peak_pressure_probability_allowed": pl.String,
        "pressure_allowed": pl.Boolean,
        "sack_allowed": pl.Float64,
        "time_to_pressure_allowed": pl.Float64,
        "quick_pressure": pl.Boolean,
        "unblocked_pressure": pl.Boolean,
        "blitzing": pl.Boolean,
        "player_get_off": pl.Float64,
        "sack": pl.Float64,
        "tackle": pl.Boolean,
        "assist": pl.Boolean,
        "caused_forced_fumble": pl.Boolean,
        "recovered_fumble": pl.Boolean,
        "tackle_for_loss": pl.Boolean,
        "time_to_pressure": pl.Float64,
        "time_to_qb_hurry": pl.Float64,
        "coverage_assignment": pl.String,
        "coverage_assignment_at_snap": pl.String,
    },

    # -------------------------------
    # games.csv
    # -------------------------------
    "games": {
        "game_id": pl.Int64,
        "game_key": pl.Int64,
        "season": pl.Int64,
        "season_type": pl.String,
        "week": pl.Int64,
        "home_team_abbr": pl.String,
        "visitor_team_abbr": pl.String,
    },

    # -------------------------------
    # game_tracking
    # -------------------------------
    "game_tracking": {
        "game_id": pl.Int64,
        "play_id": pl.Int64,
        "nfl_id": pl.Int64,
        "time": pl.String,
        "x": pl.Float64,
        "y": pl.Float64,
        "s": pl.Float64,
        "a": pl.Float64,
        "dis": pl.Float64,
        "o": pl.Float64,
        "dir": pl.Float64,
        "event": pl.String,
    }


}

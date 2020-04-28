import datajoint as dj

schema = dj.schema('calciumimaging')


@schema
class MouseSubject(dj.Manual):
    definition = """
    # subject mouse ids
    cohort_id: int # cohort for mouse subject
    subject_id : int  # id for mouse subject
    ---
    dob : date # mouse date of birth
    sex = 'U': enum('F', 'M', 'U')  # sex of mouse
    strain : varchar(10) # mouse strain
    background : varchar(20) # mouse background
    genotype : varchar(10) #mouse genotype
    comments = null : varchar(4000)
    """


@schema
class SRMTest(dj.Manual):
    definition = """
    # stimulus table
    test_name : varchar(31) # short name for test
    ---
    trials : int #number of trials
    duration : int # in minutes
    """


@schema
class RecordingSession(dj.Manual):
    definition = """
    # Calcium imaging session
    -> MouseSubject
    recording_id : int
    ---
    -> SRMTest
    experimenter : varchar(127)
    recording_quality : enum('good', 'bad', 'ugly')
    dropped_frames: longblob #an array of dropped frames
    t1posn: enum('A','B')
    t2posn: enum('A','B')
    t3posn: enum('A','B','NA')
    comments = null : varchar(4000)
    """

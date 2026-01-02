from bpy.types import PropertyGroup
from bpy.props import StringProperty, IntProperty, BoolProperty, EnumProperty, FloatProperty


def update_job(self, context):
    context.area.tag_redraw()


class CNCControlProperties(PropertyGroup):

    connection_type: EnumProperty(
        name="Type",
        default="SERIAL",
        items=[
            ("SERIAL", "Serial", "Connect via Serial Bus"),
            ("TCP", "TCP", "Connect via TCP (Transmission Control Protocol)"),
        ],
    )

    port: StringProperty(
        name="Port",
        default="/dev/ttyACM0",
        description="The port used for serial communication, often: Win: COM4, Linux: /dev/ttyACM0, Mac: /dev/tty.usbmodem...",
    )

    rate: StringProperty(
        name="Rate",
        default="115200",
        description="The rate at which comms are sent over the serial connection",
    )

    jobfile: StringProperty(
        name="Job File",
        default="",
        description="The gcode file for the job to be cut",
        subtype="FILE_PATH",
    )

    source: EnumProperty(
        name="Source",
        items=[
            ("FILE", "File", "A file loaded from disk"),
            ("TEXT", "Text", "A text block from Blender's Text Editor"),
            ("COMMAND", "Command", "A custom string entered by the user"),
        ],
        default="FILE",
    )

    command_string: StringProperty(
        name="Command",
        default="G0 X5 Y5",
        description="Enter gcode commands to be run as a job",
    )

    connected: BoolProperty(
        name="Connection Status",
        default=False,
        description="If Blender is connected to a CNC machine",
    )

    running_job: BoolProperty(
        name="Job Status",
        default=False,
        description="If a job is currently running from a gcode file",
        update=update_job,
    )

    xy_step: FloatProperty(
        name="X/Y Step Size",
        default=5,
        description="Length of the smallest movement along the X and Y axes",
    )

    z_step: FloatProperty(
        name="Z Step Size",
        default=1,
        description="Length of the smallest movement along the Z axis",
    )

    unit: StringProperty(
        name="Unit Type",
        default="G21",
        description="Metric or Imperial - Millimeter or Inch",
    )

    x_position: FloatProperty(
        name="X Position",
        default=0,
        description="Current position of the spindle along the X axis",
    )

    y_position: FloatProperty(
        name="Y Position",
        default=0,
        description="Current position of the spindle along the Y axis",
    )

    z_position: FloatProperty(
        name="Z Position",
        default=0,
        description="Current position of the spindle along the Z axis",
    )

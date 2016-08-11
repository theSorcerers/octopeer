class Api::KeystrokeEventsController < ApplicationController
  include Epochable
  include Showable
  include Indexable
  include Createable

  private

  def parameters
    params.require(:keystroke_event).permit(:keystroke, :session_id, :keystroke_type_id, :created_at)
  end
end

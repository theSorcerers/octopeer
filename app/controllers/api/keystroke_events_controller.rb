class Api::KeystrokeEventsController < ApplicationController
  include TimeHelper
  include Showable
  include Indexable
  include Createable

  private

  def keystroke_event_params
    params.require(:keystroke_event).permit(:id, :keystroke, :session_id, :keystroke_type_id, :created_at)
  end
end
